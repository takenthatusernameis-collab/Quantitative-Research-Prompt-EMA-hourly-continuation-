# EMA Hourly Continuation — SUSHI/USDT P8_89

**Symbol:** SUSHI/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 720 |
| net_profit_factor | 0.5586 |
| net_win_rate | 0.4417 |
| gross_profit_factor | 0.8281 |
| gross_win_rate | 0.4458 |
| sharpe_ratio | -5.2283 |
| sortino_ratio | -1.9568 |
| max_drawdown | 0.9111 |
| cagr | -0.6147 |
| net_avg_win | 36.2010 |
| net_avg_loss | -51.2689 |
| avg_hold_time_bars | 19.4861 |
| exposure | 0.6349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
