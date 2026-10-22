# EMA Hourly Continuation — ETHFI/USDT P12_55

**Symbol:** ETHFI/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1053 |
| net_profit_factor | 0.5696 |
| net_win_rate | 0.4435 |
| gross_profit_factor | 0.8697 |
| gross_win_rate | 0.4501 |
| sharpe_ratio | -6.2265 |
| sortino_ratio | -2.8419 |
| max_drawdown | 0.9681 |
| cagr | -0.7437 |
| net_avg_win | 27.4071 |
| net_avg_loss | -38.3472 |
| avg_hold_time_bars | 8.0522 |
| exposure | 0.3854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
