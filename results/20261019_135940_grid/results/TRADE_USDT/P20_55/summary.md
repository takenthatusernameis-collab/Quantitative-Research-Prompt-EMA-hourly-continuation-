# EMA Hourly Continuation — TRADE/USDT P20_55

**Symbol:** TRADE/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 761 |
| net_profit_factor | 0.5569 |
| net_win_rate | 0.4428 |
| gross_profit_factor | 0.8749 |
| gross_win_rate | 0.4455 |
| sharpe_ratio | -5.9517 |
| sortino_ratio | -2.2790 |
| max_drawdown | 0.9470 |
| cagr | -0.6838 |
| net_avg_win | 35.2301 |
| net_avg_loss | -50.2776 |
| avg_hold_time_bars | 6.8331 |
| exposure | 0.2364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
