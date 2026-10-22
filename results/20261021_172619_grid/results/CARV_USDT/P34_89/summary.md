# EMA Hourly Continuation — CARV/USDT P34_89

**Symbol:** CARV/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.6183 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.8129 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -2.9825 |
| sortino_ratio | -0.8521 |
| max_drawdown | 0.5748 |
| cagr | -0.3241 |
| net_avg_win | 60.4069 |
| net_avg_loss | -80.2376 |
| avg_hold_time_bars | 11.7362 |
| exposure | 0.2153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
