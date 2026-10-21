# EMA Hourly Continuation — SEI/USDT P21_200

**Symbol:** SEI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 1.0494 |
| net_win_rate | 0.5522 |
| gross_profit_factor | 1.2139 |
| gross_win_rate | 0.5522 |
| sharpe_ratio | 0.3058 |
| sortino_ratio | 0.0727 |
| max_drawdown | 0.1465 |
| cagr | 0.0265 |
| net_avg_win | 97.4988 |
| net_avg_loss | -114.5891 |
| avg_hold_time_bars | 52.6418 |
| exposure | 0.6413 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
