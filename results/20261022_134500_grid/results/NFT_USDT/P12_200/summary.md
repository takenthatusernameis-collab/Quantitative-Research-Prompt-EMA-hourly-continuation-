# EMA Hourly Continuation — NFT/USDT P12_200

**Symbol:** NFT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.2872 |
| net_win_rate | 0.2704 |
| gross_profit_factor | 0.6584 |
| gross_win_rate | 0.3039 |
| sharpe_ratio | -13.3522 |
| sortino_ratio | -5.4237 |
| max_drawdown | 0.9993 |
| cagr | -0.9450 |
| net_avg_win | 19.9346 |
| net_avg_loss | -25.7247 |
| avg_hold_time_bars | 19.7028 |
| exposure | 0.6690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
