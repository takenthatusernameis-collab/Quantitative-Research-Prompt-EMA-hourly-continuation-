# EMA Hourly Continuation — COTI/USDT P55_100

**Symbol:** COTI/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.5323 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.8584 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -4.5227 |
| sortino_ratio | -1.6487 |
| max_drawdown | 0.8612 |
| cagr | -0.5444 |
| net_avg_win | 31.1113 |
| net_avg_loss | -52.9066 |
| avg_hold_time_bars | 4.8446 |
| exposure | 0.1460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
