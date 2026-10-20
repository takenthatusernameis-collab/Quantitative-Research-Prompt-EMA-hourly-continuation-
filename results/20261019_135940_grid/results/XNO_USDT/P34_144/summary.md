# EMA Hourly Continuation — XNO/USDT P34_144

**Symbol:** XNO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.5392 |
| net_win_rate | 0.4211 |
| gross_profit_factor | 0.8223 |
| gross_win_rate | 0.4241 |
| sharpe_ratio | -5.9476 |
| sortino_ratio | -2.1696 |
| max_drawdown | 0.9281 |
| cagr | -0.6495 |
| net_avg_win | 38.3729 |
| net_avg_loss | -51.7762 |
| avg_hold_time_bars | 11.8810 |
| exposure | 0.3629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
