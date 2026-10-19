# EMA Hourly Continuation — ARB/USDT P50_144

**Symbol:** ARB/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.6605 |
| net_win_rate | 0.5060 |
| gross_profit_factor | 1.0029 |
| gross_win_rate | 0.5100 |
| sharpe_ratio | -2.6536 |
| sortino_ratio | -0.8373 |
| max_drawdown | 0.6335 |
| cagr | -0.3295 |
| net_avg_win | 48.5162 |
| net_avg_loss | -75.2341 |
| avg_hold_time_bars | 11.8486 |
| exposure | 0.2704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
