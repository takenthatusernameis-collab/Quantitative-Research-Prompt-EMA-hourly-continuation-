# EMA Hourly Continuation — EGLD/USDT P8_20

**Symbol:** EGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1654 |
| net_profit_factor | 0.3028 |
| net_win_rate | 0.4166 |
| gross_profit_factor | 0.8362 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -13.0998 |
| sortino_ratio | -7.5232 |
| max_drawdown | 0.9999 |
| cagr | -0.9793 |
| net_avg_win | 6.3023 |
| net_avg_loss | -14.8618 |
| avg_hold_time_bars | 2.8724 |
| exposure | 0.2160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
