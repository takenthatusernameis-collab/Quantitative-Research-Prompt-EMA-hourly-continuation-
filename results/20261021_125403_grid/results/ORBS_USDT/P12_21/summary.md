# EMA Hourly Continuation — ORBS/USDT P12_21

**Symbol:** ORBS/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.4801 |
| net_win_rate | 0.4101 |
| gross_profit_factor | 0.8014 |
| gross_win_rate | 0.4101 |
| sharpe_ratio | -5.6608 |
| sortino_ratio | -1.7353 |
| max_drawdown | 0.8711 |
| cagr | -0.5537 |
| net_avg_win | 42.8684 |
| net_avg_loss | -62.0742 |
| avg_hold_time_bars | 7.7719 |
| exposure | 0.1611 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
