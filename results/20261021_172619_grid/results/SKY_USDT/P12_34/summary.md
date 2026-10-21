# EMA Hourly Continuation — SKY/USDT P12_34

**Symbol:** SKY/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.6806 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 0.9820 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -3.3667 |
| sortino_ratio | -1.2617 |
| max_drawdown | 0.6966 |
| cagr | -0.4378 |
| net_avg_win | 54.0350 |
| net_avg_loss | -76.3209 |
| avg_hold_time_bars | 6.8097 |
| exposure | 0.2115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
