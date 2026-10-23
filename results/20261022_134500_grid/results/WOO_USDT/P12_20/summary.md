# EMA Hourly Continuation — WOO/USDT P12_20

**Symbol:** WOO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1455 |
| net_profit_factor | 0.3334 |
| net_win_rate | 0.3945 |
| gross_profit_factor | 0.8220 |
| gross_win_rate | 0.4302 |
| sharpe_ratio | -13.0960 |
| sortino_ratio | -7.1222 |
| max_drawdown | 0.9999 |
| cagr | -0.9735 |
| net_avg_win | 8.7117 |
| net_avg_loss | -17.0254 |
| avg_hold_time_bars | 2.4584 |
| exposure | 0.1626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
