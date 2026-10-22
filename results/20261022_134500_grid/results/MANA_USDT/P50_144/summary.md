# EMA Hourly Continuation — MANA/USDT P50_144

**Symbol:** MANA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.5696 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.9491 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -4.1244 |
| sortino_ratio | -1.2990 |
| max_drawdown | 0.7951 |
| cagr | -0.4646 |
| net_avg_win | 44.5773 |
| net_avg_loss | -69.4060 |
| avg_hold_time_bars | 13.5900 |
| exposure | 0.3089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
