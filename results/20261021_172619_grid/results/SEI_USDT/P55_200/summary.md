# EMA Hourly Continuation — SEI/USDT P55_200

**Symbol:** SEI/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.8517 |
| net_win_rate | 0.5076 |
| gross_profit_factor | 1.0146 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -0.7749 |
| sortino_ratio | -0.1803 |
| max_drawdown | 0.2292 |
| cagr | -0.0813 |
| net_avg_win | 82.1529 |
| net_avg_loss | -99.4267 |
| avg_hold_time_bars | 30.4280 |
| exposure | 0.3651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
