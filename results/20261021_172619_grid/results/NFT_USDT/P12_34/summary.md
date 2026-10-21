# EMA Hourly Continuation — NFT/USDT P12_34

**Symbol:** NFT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.3163 |
| net_win_rate | 0.2803 |
| gross_profit_factor | 0.5822 |
| gross_win_rate | 0.2845 |
| sharpe_ratio | -9.6975 |
| sortino_ratio | -3.1316 |
| max_drawdown | 0.9783 |
| cagr | -0.7824 |
| net_avg_win | 33.7759 |
| net_avg_loss | -41.5957 |
| avg_hold_time_bars | 8.0983 |
| exposure | 0.1760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
