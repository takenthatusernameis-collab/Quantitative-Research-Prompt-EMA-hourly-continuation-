# EMA Hourly Continuation — WIN/USDT P8_26

**Symbol:** WIN/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 625 |
| net_profit_factor | 0.6522 |
| net_win_rate | 0.4944 |
| gross_profit_factor | 1.0113 |
| gross_win_rate | 0.4944 |
| sharpe_ratio | -3.5456 |
| sortino_ratio | -1.2761 |
| max_drawdown | 0.7682 |
| cagr | -0.4413 |
| net_avg_win | 46.6087 |
| net_avg_loss | -69.8856 |
| avg_hold_time_bars | 7.7264 |
| exposure | 0.2195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
