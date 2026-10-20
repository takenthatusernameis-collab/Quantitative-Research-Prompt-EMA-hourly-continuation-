# EMA Hourly Continuation — CARV/USDT P12_55

**Symbol:** CARV/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.6387 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 1.0106 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -4.2682 |
| sortino_ratio | -1.7830 |
| max_drawdown | 0.8220 |
| cagr | -0.5695 |
| net_avg_win | 42.0967 |
| net_avg_loss | -62.6295 |
| avg_hold_time_bars | 10.3796 |
| exposure | 0.4124 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
