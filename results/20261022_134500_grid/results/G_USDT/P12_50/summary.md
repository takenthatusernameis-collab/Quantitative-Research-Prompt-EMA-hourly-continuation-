# EMA Hourly Continuation — G/USDT P12_50

**Symbol:** G/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 807 |
| net_profit_factor | 0.5402 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.8852 |
| gross_win_rate | 0.4696 |
| sharpe_ratio | -6.0193 |
| sortino_ratio | -2.5975 |
| max_drawdown | 0.9326 |
| cagr | -0.7104 |
| net_avg_win | 29.9242 |
| net_avg_loss | -45.9714 |
| avg_hold_time_bars | 9.4746 |
| exposure | 0.4020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
