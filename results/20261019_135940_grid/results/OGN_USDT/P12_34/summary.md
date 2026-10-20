# EMA Hourly Continuation — OGN/USDT P12_34

**Symbol:** OGN/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1203 |
| net_profit_factor | 0.4839 |
| net_win_rate | 0.4347 |
| gross_profit_factor | 0.9357 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -9.0344 |
| sortino_ratio | -4.4010 |
| max_drawdown | 0.9960 |
| cagr | -0.8870 |
| net_avg_win | 17.8578 |
| net_avg_loss | -28.3806 |
| avg_hold_time_bars | 4.7174 |
| exposure | 0.2568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
