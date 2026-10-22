# EMA Hourly Continuation — MEW/USDT P12_26

**Symbol:** MEW/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.6945 |
| net_win_rate | 0.4779 |
| gross_profit_factor | 0.9133 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -2.8640 |
| sortino_ratio | -0.9547 |
| max_drawdown | 0.7002 |
| cagr | -0.3547 |
| net_avg_win | 58.3340 |
| net_avg_loss | -76.8941 |
| avg_hold_time_bars | 5.1195 |
| exposure | 0.1266 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
