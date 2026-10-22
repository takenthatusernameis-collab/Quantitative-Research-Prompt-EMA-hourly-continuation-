# EMA Hourly Continuation — ETH/USDT P26_200

**Symbol:** ETH/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.5192 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9611 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -3.2478 |
| sortino_ratio | -0.7735 |
| max_drawdown | 0.6325 |
| cagr | -0.3163 |
| net_avg_win | 48.1307 |
| net_avg_loss | -84.7261 |
| avg_hold_time_bars | 49.4983 |
| exposure | 0.6502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
