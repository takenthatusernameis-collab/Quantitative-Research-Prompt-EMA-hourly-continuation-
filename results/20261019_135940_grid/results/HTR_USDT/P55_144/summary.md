# EMA Hourly Continuation — HTR/USDT P55_144

**Symbol:** HTR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.4540 |
| net_win_rate | 0.3841 |
| gross_profit_factor | 0.6741 |
| gross_win_rate | 0.3952 |
| sharpe_ratio | -6.9264 |
| sortino_ratio | -2.4479 |
| max_drawdown | 0.9558 |
| cagr | -0.7002 |
| net_avg_win | 32.6926 |
| net_avg_loss | -44.9124 |
| avg_hold_time_bars | 8.1730 |
| exposure | 0.2340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
