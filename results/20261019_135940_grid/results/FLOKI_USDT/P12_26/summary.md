# EMA Hourly Continuation — FLOKI/USDT P12_26

**Symbol:** FLOKI/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1452 |
| net_profit_factor | 0.4027 |
| net_win_rate | 0.3898 |
| gross_profit_factor | 0.7299 |
| gross_win_rate | 0.4112 |
| sharpe_ratio | -12.7317 |
| sortino_ratio | -6.8631 |
| max_drawdown | 0.9999 |
| cagr | -0.9704 |
| net_avg_win | 11.9109 |
| net_avg_loss | -18.8940 |
| avg_hold_time_bars | 2.8361 |
| exposure | 0.1872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
