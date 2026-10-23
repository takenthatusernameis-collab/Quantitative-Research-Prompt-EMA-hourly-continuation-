# EMA Hourly Continuation — WEMIX/USDT P26_144

**Symbol:** WEMIX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 757 |
| net_profit_factor | 0.3278 |
| net_win_rate | 0.3078 |
| gross_profit_factor | 0.5072 |
| gross_win_rate | 0.3197 |
| sharpe_ratio | -10.6059 |
| sortino_ratio | -4.1439 |
| max_drawdown | 0.9949 |
| cagr | -0.8766 |
| net_avg_win | 20.8228 |
| net_avg_loss | -28.2433 |
| avg_hold_time_bars | 15.4518 |
| exposure | 0.5317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
