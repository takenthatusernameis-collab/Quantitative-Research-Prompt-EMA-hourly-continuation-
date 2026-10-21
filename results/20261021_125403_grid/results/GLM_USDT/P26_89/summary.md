# EMA Hourly Continuation — GLM/USDT P26_89

**Symbol:** GLM/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.6655 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9058 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -2.7322 |
| sortino_ratio | -0.8978 |
| max_drawdown | 0.6553 |
| cagr | -0.3370 |
| net_avg_win | 50.2200 |
| net_avg_loss | -70.2295 |
| avg_hold_time_bars | 13.0246 |
| exposure | 0.3132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
