# EMA Hourly Continuation — ILV/USDT P26_144

**Symbol:** ILV/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.9080 |
| net_win_rate | 0.5296 |
| gross_profit_factor | 1.1207 |
| gross_win_rate | 0.5296 |
| sharpe_ratio | -0.5741 |
| sortino_ratio | -0.1669 |
| max_drawdown | 0.2368 |
| cagr | -0.0779 |
| net_avg_win | 84.5072 |
| net_avg_loss | -104.7691 |
| avg_hold_time_bars | 24.9951 |
| exposure | 0.4613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
