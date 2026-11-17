# EMA Hourly Continuation — NUM/USDT P21_200

**Symbol:** NUM/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.5762 |
| net_win_rate | 0.4187 |
| gross_profit_factor | 0.7579 |
| gross_win_rate | 0.4211 |
| sharpe_ratio | -3.7905 |
| sortino_ratio | -1.0843 |
| max_drawdown | 0.7400 |
| cagr | -0.4031 |
| net_avg_win | 56.4327 |
| net_avg_loss | -70.5321 |
| avg_hold_time_bars | 31.8158 |
| exposure | 0.6045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
