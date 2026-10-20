# EMA Hourly Continuation — FLUX/USDT P8_89

**Symbol:** FLUX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.6685 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 0.9963 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -3.3738 |
| sortino_ratio | -1.2858 |
| max_drawdown | 0.8103 |
| cagr | -0.4600 |
| net_avg_win | 43.9642 |
| net_avg_loss | -63.6533 |
| avg_hold_time_bars | 19.2316 |
| exposure | 0.6416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
