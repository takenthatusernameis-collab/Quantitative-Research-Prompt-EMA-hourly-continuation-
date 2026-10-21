# EMA Hourly Continuation — NFT/USDT P50_200

**Symbol:** NFT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.4307 |
| net_win_rate | 0.3797 |
| gross_profit_factor | 0.7139 |
| gross_win_rate | 0.3797 |
| sharpe_ratio | -5.8037 |
| sortino_ratio | -1.6151 |
| max_drawdown | 0.8514 |
| cagr | -0.5304 |
| net_avg_win | 45.2850 |
| net_avg_loss | -64.3612 |
| avg_hold_time_bars | 21.3369 |
| exposure | 0.3627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
