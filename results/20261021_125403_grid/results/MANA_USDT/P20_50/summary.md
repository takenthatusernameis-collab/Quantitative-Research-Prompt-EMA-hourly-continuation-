# EMA Hourly Continuation — MANA/USDT P20_50

**Symbol:** MANA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.7211 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 0.9935 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -2.5699 |
| sortino_ratio | -0.8353 |
| max_drawdown | 0.6416 |
| cagr | -0.3174 |
| net_avg_win | 63.2671 |
| net_avg_loss | -84.3915 |
| avg_hold_time_bars | 7.7957 |
| exposure | 0.1821 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
