# EMA Hourly Continuation — KCS/USDT P34_144

**Symbol:** KCS/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.3535 |
| net_win_rate | 0.4038 |
| gross_profit_factor | 0.8383 |
| gross_win_rate | 0.4435 |
| sharpe_ratio | -6.9477 |
| sortino_ratio | -2.1444 |
| max_drawdown | 0.9404 |
| cagr | -0.6713 |
| net_avg_win | 26.5971 |
| net_avg_loss | -50.9526 |
| avg_hold_time_bars | 19.1318 |
| exposure | 0.4157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
