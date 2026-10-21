# EMA Hourly Continuation — NFT/USDT P34_200

**Symbol:** NFT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.4326 |
| net_win_rate | 0.3879 |
| gross_profit_factor | 0.6866 |
| gross_win_rate | 0.3879 |
| sharpe_ratio | -5.3049 |
| sortino_ratio | -1.4190 |
| max_drawdown | 0.8179 |
| cagr | -0.4866 |
| net_avg_win | 45.8970 |
| net_avg_loss | -67.2374 |
| avg_hold_time_bars | 31.8448 |
| exposure | 0.5037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
