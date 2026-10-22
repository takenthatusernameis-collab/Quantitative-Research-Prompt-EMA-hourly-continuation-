# EMA Hourly Continuation — SOL/USDT P8_34

**Symbol:** SOL/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1349 |
| net_profit_factor | 0.4852 |
| net_win_rate | 0.4433 |
| gross_profit_factor | 0.9494 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -9.4802 |
| sortino_ratio | -4.8686 |
| max_drawdown | 0.9981 |
| cagr | -0.9171 |
| net_avg_win | 15.7301 |
| net_avg_loss | -25.8154 |
| avg_hold_time_bars | 5.1683 |
| exposure | 0.3169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
