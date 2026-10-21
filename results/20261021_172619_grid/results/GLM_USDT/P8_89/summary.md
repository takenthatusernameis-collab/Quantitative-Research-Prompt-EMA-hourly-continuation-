# EMA Hourly Continuation — GLM/USDT P8_89

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.7522 |
| net_win_rate | 0.4941 |
| gross_profit_factor | 0.9790 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -2.2171 |
| sortino_ratio | -0.7741 |
| max_drawdown | 0.6194 |
| cagr | -0.3001 |
| net_avg_win | 60.9051 |
| net_avg_loss | -79.0901 |
| avg_hold_time_bars | 22.5276 |
| exposure | 0.6113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
