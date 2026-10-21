# EMA Hourly Continuation — ENS/USDT P8_200

**Symbol:** ENS/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.8510 |
| net_win_rate | 0.5038 |
| gross_profit_factor | 1.0050 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -0.7356 |
| sortino_ratio | -0.1698 |
| max_drawdown | 0.2858 |
| cagr | -0.0770 |
| net_avg_win | 79.5060 |
| net_avg_loss | -94.8766 |
| avg_hold_time_bars | 69.6885 |
| exposure | 0.8236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
