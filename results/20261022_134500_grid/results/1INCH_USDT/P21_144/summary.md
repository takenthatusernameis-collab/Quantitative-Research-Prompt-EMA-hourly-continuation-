# EMA Hourly Continuation — 1INCH/USDT P21_144

**Symbol:** 1INCH/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.6066 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.9166 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -3.9000 |
| sortino_ratio | -1.1896 |
| max_drawdown | 0.7825 |
| cagr | -0.4392 |
| net_avg_win | 54.4263 |
| net_avg_loss | -76.0578 |
| avg_hold_time_bars | 27.5391 |
| exposure | 0.5921 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
