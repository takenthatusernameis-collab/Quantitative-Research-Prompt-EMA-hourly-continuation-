# EMA Hourly Continuation — STX/USDT P20_144

**Symbol:** STX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.8471 |
| net_win_rate | 0.5072 |
| gross_profit_factor | 1.0186 |
| gross_win_rate | 0.5072 |
| sharpe_ratio | -0.8840 |
| sortino_ratio | -0.2362 |
| max_drawdown | 0.2996 |
| cagr | -0.1050 |
| net_avg_win | 76.4011 |
| net_avg_loss | -92.8083 |
| avg_hold_time_bars | 35.8911 |
| exposure | 0.5668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
