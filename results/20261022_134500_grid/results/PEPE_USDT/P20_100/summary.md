# EMA Hourly Continuation — PEPE/USDT P20_100

**Symbol:** PEPE/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.5797 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.8404 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -4.6020 |
| sortino_ratio | -1.5491 |
| max_drawdown | 0.8496 |
| cagr | -0.5266 |
| net_avg_win | 45.8143 |
| net_avg_loss | -62.7840 |
| avg_hold_time_bars | 17.5677 |
| exposure | 0.4600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
