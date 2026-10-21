# EMA Hourly Continuation — ZEN/USDT P20_55

**Symbol:** ZEN/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.7244 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9544 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -2.2909 |
| sortino_ratio | -0.7804 |
| max_drawdown | 0.6191 |
| cagr | -0.3022 |
| net_avg_win | 56.0438 |
| net_avg_loss | -74.9467 |
| avg_hold_time_bars | 7.8448 |
| exposure | 0.2022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
