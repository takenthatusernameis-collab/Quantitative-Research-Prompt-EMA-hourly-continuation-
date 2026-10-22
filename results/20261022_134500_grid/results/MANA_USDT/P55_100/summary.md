# EMA Hourly Continuation — MANA/USDT P55_100

**Symbol:** MANA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.4185 |
| net_win_rate | 0.4209 |
| gross_profit_factor | 0.8158 |
| gross_win_rate | 0.4507 |
| sharpe_ratio | -7.3367 |
| sortino_ratio | -2.6660 |
| max_drawdown | 0.9676 |
| cagr | -0.7439 |
| net_avg_win | 24.6847 |
| net_avg_loss | -42.8718 |
| avg_hold_time_bars | 4.9910 |
| exposure | 0.1520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
