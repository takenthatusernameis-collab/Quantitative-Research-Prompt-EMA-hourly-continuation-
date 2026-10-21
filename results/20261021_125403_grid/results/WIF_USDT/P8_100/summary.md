# EMA Hourly Continuation — WIF/USDT P8_100

**Symbol:** WIF/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.8255 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.9477 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -1.3021 |
| sortino_ratio | -0.3944 |
| max_drawdown | 0.4739 |
| cagr | -0.1684 |
| net_avg_win | 79.6751 |
| net_avg_loss | -91.9264 |
| avg_hold_time_bars | 31.3481 |
| exposure | 0.6426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
