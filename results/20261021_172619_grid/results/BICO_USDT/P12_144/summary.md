# EMA Hourly Continuation — BICO/USDT P12_144

**Symbol:** BICO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.8583 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0071 |
| gross_win_rate | 0.5042 |
| sharpe_ratio | -0.8603 |
| sortino_ratio | -0.2327 |
| max_drawdown | 0.3322 |
| cagr | -0.1044 |
| net_avg_win | 81.3801 |
| net_avg_loss | -96.4188 |
| avg_hold_time_bars | 42.8319 |
| exposure | 0.6950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
