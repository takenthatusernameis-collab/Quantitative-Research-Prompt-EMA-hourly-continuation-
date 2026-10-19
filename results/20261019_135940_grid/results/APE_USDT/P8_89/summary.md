# EMA Hourly Continuation — APE/USDT P8_89

**Symbol:** APE/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 717 |
| net_profit_factor | 0.6520 |
| net_win_rate | 0.4714 |
| gross_profit_factor | 1.0075 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -4.1355 |
| sortino_ratio | -1.5654 |
| max_drawdown | 0.8507 |
| cagr | -0.5205 |
| net_avg_win | 46.6714 |
| net_avg_loss | -63.8406 |
| avg_hold_time_bars | 20.0126 |
| exposure | 0.6522 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
