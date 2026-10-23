# EMA Hourly Continuation — AEVO/USDT P12_89

**Symbol:** AEVO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.6988 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 1.0030 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -3.6071 |
| sortino_ratio | -1.3234 |
| max_drawdown | 0.8169 |
| cagr | -0.4637 |
| net_avg_win | 57.0836 |
| net_avg_loss | -74.3055 |
| avg_hold_time_bars | 18.6391 |
| exposure | 0.5702 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
