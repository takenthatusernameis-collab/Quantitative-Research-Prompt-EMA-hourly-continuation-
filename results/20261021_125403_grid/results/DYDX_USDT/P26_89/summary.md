# EMA Hourly Continuation — DYDX/USDT P26_89

**Symbol:** DYDX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.7207 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9015 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -2.0848 |
| sortino_ratio | -0.6371 |
| max_drawdown | 0.5456 |
| cagr | -0.2535 |
| net_avg_win | 61.0100 |
| net_avg_loss | -77.5962 |
| avg_hold_time_bars | 15.4717 |
| exposure | 0.3235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
