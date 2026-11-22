# EMA Hourly Continuation — AZERO/USDT P12_21

**Symbol:** AZERO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1291 |
| net_profit_factor | 0.3053 |
| net_win_rate | 0.3826 |
| gross_profit_factor | 0.8183 |
| gross_win_rate | 0.4175 |
| sharpe_ratio | -12.1721 |
| sortino_ratio | -6.2005 |
| max_drawdown | 0.9997 |
| cagr | -0.9574 |
| net_avg_win | 8.8941 |
| net_avg_loss | -18.0555 |
| avg_hold_time_bars | 3.0302 |
| exposure | 0.1770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
