# EMA Hourly Continuation — REQ/USDT P8_34

**Symbol:** REQ/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1385 |
| net_profit_factor | 0.3620 |
| net_win_rate | 0.3870 |
| gross_profit_factor | 0.7621 |
| gross_win_rate | 0.4152 |
| sharpe_ratio | -12.8618 |
| sortino_ratio | -6.8087 |
| max_drawdown | 0.9998 |
| cagr | -0.9691 |
| net_avg_win | 10.5839 |
| net_avg_loss | -18.4586 |
| avg_hold_time_bars | 6.1018 |
| exposure | 0.3841 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
