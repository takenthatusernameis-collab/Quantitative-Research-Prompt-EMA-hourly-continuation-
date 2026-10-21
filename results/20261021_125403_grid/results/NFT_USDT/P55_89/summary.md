# EMA Hourly Continuation — NFT/USDT P55_89

**Symbol:** NFT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.2777 |
| net_win_rate | 0.2867 |
| gross_profit_factor | 0.5803 |
| gross_win_rate | 0.2900 |
| sharpe_ratio | -7.6777 |
| sortino_ratio | -1.9698 |
| max_drawdown | 0.9051 |
| cagr | -0.6085 |
| net_avg_win | 40.4567 |
| net_avg_loss | -58.5536 |
| avg_hold_time_bars | 8.7333 |
| exposure | 0.1191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
