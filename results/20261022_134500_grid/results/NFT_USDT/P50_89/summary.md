# EMA Hourly Continuation — NFT/USDT P50_89

**Symbol:** NFT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1238 |
| net_profit_factor | 0.1631 |
| net_win_rate | 0.1922 |
| gross_profit_factor | 0.5591 |
| gross_win_rate | 0.2496 |
| sharpe_ratio | -21.4866 |
| sortino_ratio | -11.9808 |
| max_drawdown | 1.0000 |
| cagr | -0.9986 |
| net_avg_win | 8.1904 |
| net_avg_loss | -11.9493 |
| avg_hold_time_bars | 3.6333 |
| exposure | 0.2045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
