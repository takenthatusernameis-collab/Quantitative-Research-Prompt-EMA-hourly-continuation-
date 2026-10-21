# EMA Hourly Continuation — ATH/USDT P50_89

**Symbol:** ATH/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.7788 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 0.9955 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -1.3197 |
| sortino_ratio | -0.3372 |
| max_drawdown | 0.3274 |
| cagr | -0.1439 |
| net_avg_win | 71.9276 |
| net_avg_loss | -93.6006 |
| avg_hold_time_bars | 7.4732 |
| exposure | 0.1079 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
