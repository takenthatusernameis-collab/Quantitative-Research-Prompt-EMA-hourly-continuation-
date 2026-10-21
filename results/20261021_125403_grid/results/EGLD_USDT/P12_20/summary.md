# EMA Hourly Continuation — EGLD/USDT P12_20

**Symbol:** EGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.6664 |
| net_win_rate | 0.4864 |
| gross_profit_factor | 0.9856 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -2.5132 |
| sortino_ratio | -0.6568 |
| max_drawdown | 0.5514 |
| cagr | -0.2595 |
| net_avg_win | 65.7181 |
| net_avg_loss | -93.4019 |
| avg_hold_time_bars | 4.7915 |
| exposure | 0.0721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
