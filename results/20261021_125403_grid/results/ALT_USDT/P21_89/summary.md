# EMA Hourly Continuation — ALT/USDT P21_89

**Symbol:** ALT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.7846 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 0.9726 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -1.6753 |
| sortino_ratio | -0.5409 |
| max_drawdown | 0.4860 |
| cagr | -0.2214 |
| net_avg_win | 67.2080 |
| net_avg_loss | -84.3206 |
| avg_hold_time_bars | 15.2196 |
| exposure | 0.3528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
