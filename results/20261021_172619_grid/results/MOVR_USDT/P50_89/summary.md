# EMA Hourly Continuation — MOVR/USDT P50_89

**Symbol:** MOVR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.5885 |
| net_win_rate | 0.4392 |
| gross_profit_factor | 0.7843 |
| gross_win_rate | 0.4392 |
| sharpe_ratio | -3.2324 |
| sortino_ratio | -0.8929 |
| max_drawdown | 0.6758 |
| cagr | -0.3373 |
| net_avg_win | 55.4819 |
| net_avg_loss | -73.8259 |
| avg_hold_time_bars | 7.3466 |
| exposure | 0.1262 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
