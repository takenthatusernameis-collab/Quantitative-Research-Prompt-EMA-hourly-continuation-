# EMA Hourly Continuation — NFT/USDT P20_200

**Symbol:** NFT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 742 |
| net_profit_factor | 0.2722 |
| net_win_rate | 0.2736 |
| gross_profit_factor | 0.5986 |
| gross_win_rate | 0.3032 |
| sharpe_ratio | -13.4306 |
| sortino_ratio | -5.4233 |
| max_drawdown | 0.9994 |
| cagr | -0.9484 |
| net_avg_win | 18.4095 |
| net_avg_loss | -25.4755 |
| avg_hold_time_bars | 17.5863 |
| exposure | 0.5931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
